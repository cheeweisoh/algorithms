import javax.swing.tree.TreeNode;

class Solution {
    private TreeNode addRow(TreeNode node, int val, int depth, int curr) {
        if (node == null) {
            return null;
        }

        if (curr == depth - 1) {
            TreeNode leftTemp = node.left, rightTemp = node.right;

            node.left = new TreeNode(val);
            node.left.left = leftTemp;
            node.right = new TreeNode(val);
            node.right.right = rightTemp;

            return node;
        }

        node.left = addRow(node.left, val, depth, curr + 1);
        node.right = addRow(node.right, val, depth, curr + 1);

        return node;
    }

    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            TreeNode newRoot = new TreeNode(val);
            newRoot.left = root;
            return newRoot;
        }

        return add(root, val, depth, 1);
    }
}
