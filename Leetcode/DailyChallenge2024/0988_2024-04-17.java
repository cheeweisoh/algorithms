class Solution {
    private class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public String smallestFromLeaf(TreeNode root) {
        StringBuilder ans = new StringBuilder();
        dfs(root, new StringBuilder(), ans);

        return ans.toString();
    }

    private void dfs(TreeNode node, StringBuilder path, StringBuilder smallest) {
       if (node == null) return;
       
       path.append((char)('a' + node.val));

       if (node.left == null && node.right == null) {
            String currString = path.reverse().toString();
            if (smallest.length() == 0 || currString.compareTo(smallest.toString()) < 0) {
                smallest.setLength(0);
                smallest.append(currString);
            }
            path.reverse();
       }

       dfs(node.left, path, smallest);
       dfs(node.right, path, smallest);

       path.setLength(path.length() - 1);
    }
}