/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/*
* Good test cases
*
* Case 1
* root1 = [1,3,2,5]
* root2 = [2,1,3,null,4,null,7]
*
* Case 2
* root1 = [1]
* root2 = [1,2]
*/

function mergeTrees(root1, root2) {
    if (!root1) return root2
    if (!root2) return root1

    const mergedNode = new TreeNode(
        root1.val += root2.val,
        mergeTrees(root1.left, root2.left),
        mergeTrees(root1.right, root2.right)
    )

    return mergedNode
};