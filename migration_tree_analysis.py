from ete3 import Tree, TreeStyle, NodeStyle, TextFace
import os
from collections import defaultdict

# Input and output
nwk_file = r"results/example_tree.nwk"
output_pdf = nwk_file + ".migration.pdf"

# Load tree
with open(nwk_file, "r") as f:
    newick_str = f.read().strip()

# Fix special characters
newick_str = newick_str.replace("-.", "_")

t = Tree(newick_str, format=1)
t.unroot()

# Extract country code
def get_country(name):
    parts = name.split(".")
    if len(parts) > 1:
        return parts[1]
    return "UNK"

for leaf in t:
    leaf.add_feature("country", get_country(leaf.name))

# Infer ancestral locations (simple parsimony)
def assign_ancestral_country(node):
    if node.is_leaf():
        return set([node.country])
    child_sets = [assign_ancestral_country(c) for c in node.get_children()]
    intersection = set.intersection(*child_sets)
    if intersection:
        node.add_feature("country", list(intersection)[0])
        return intersection
    else:
        node.add_feature("country", list(child_sets[0])[0])
        return set([node.country])

assign_ancestral_country(t)

# Collect migrations
migrations = []
for node in t.traverse():
    for child in node.children:
        if node.country != child.country:
            migrations.append((node.country, child.country))

print("Migration Events:")
for i, (frm, to) in enumerate(migrations, 1):
    print(f"{i}. {frm} → {to}")

# Map countries to colors
countries = list(set([leaf.country for leaf in t]))
colors = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "brown", "pink", "lime"]
color_map = {c: colors[i % len(colors)] for i, c in enumerate(countries)}

# Apply styles
for node in t.traverse():
    ns = NodeStyle()
    ns["fgcolor"] = color_map.get(node.country, "black")
    ns["size"] = 10
    node.set_style(ns)

# Tree style
ts = TreeStyle()
ts.show_leaf_name = True
ts.mode = "c"
ts.title.add_face(TextFace("HIV Migration Tree", fsize=20), column=0)

# Render
t.render(output_pdf, w=2000, tree_style=ts)
print(f"Migration tree saved to: {output_pdf}")
