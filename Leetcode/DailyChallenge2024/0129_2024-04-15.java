import javax.swing.tree.TreeNode;

class Solution {
    private int dfs(TreeNode node, int pathSum) {
        if (node == null) {
            return 0;
        }

        if (node.left == null && node.right == null) {
            return pathSum + node.val;
        }

        int total = 0;
        pathSum += node.val;
        if (node.left != null) {
            total += dfs(node.left, pathSum * 10);
        }
        if (node.right != null) {
            total += dfs(node.right, pathSum * 10);
        }

        return total;
    }

    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }
}
