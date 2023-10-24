// Java program to Get Level of a node in a Binary Tree
/* A tree node structure */
class Node {
	int data;
	Node left, right;

	public Node(int d)
	{
		data = d;
		left = right = null;
	}
}

class BinaryTree {

	Node root;

	// Helper function for getLevel(). It returns level of
	// the data if data is present in tree, otherwise
	// returns 0.
	int getLevelUtil(Node node, int data, int level)
	{
		if (node == null)
			return 0;

		if (node.data == data)
			return level;

		int downlevel
			= getLevelUtil(node.left, data, level + 1);
		if (downlevel != 0)
			return downlevel;

		downlevel
			= getLevelUtil(node.right, data, level + 1);
		return downlevel;
	}

	/* Returns level of given data value */
	int getLevel(Node node, int data)
	{
		return getLevelUtil(node, data, 1);
	}

	/* Driver code */
	public static void main(String[] args)
	{
		BinaryTree tree = new BinaryTree();

		/* Constructing tree given in the above figure */
		tree.root = new Node(3);
		tree.root.left = new Node(2);
		tree.root.right = new Node(5);
		tree.root.left.left = new Node(1);
		tree.root.left.right = new Node(4);
		for (int x = 1; x <= 5; x++) {
			int level = tree.getLevel(tree.root, x);
			if (level != 0)
				System.out.println(
					"Level of " + x + " is "
					+ tree.getLevel(tree.root, x));
			else
				System.out.println(
					x + " is not present in tree");
		}
	}
}

// This code is contributed by Aditya Kumar (adityakumar129)
