//Graph Implementation using LinkedList (adjacency list approach)

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Graph {
 private LinkedList<Integer> adj[];
 public Graph(int vertices) {
  adj=new LinkedList[vertices];
  for(int i=0;i<vertices;i++) {
   adj[i]=new LinkedList<Integer>();
  
  }
  int count=0;
 }
  }
 public void addedge(int source,int destination) {

  adj[source].add(destination);
  adj[destination].add(source);
 }
 

 public static void main(String[] args) {
  Scanner sc=new Scanner(System.in);


  System.out.println("Enter no. of Vertices and no. of edges");
  int v=sc.nextInt();
  int e=sc.nextInt();
  int [][] gra=new int[v][v];
  int [][] ver=new int[e][2];
  Graph graph=new Graph(v+1);
  System.out.println("Enter the "+ e +" edges");
  for(int i=0;i<e;i++){
   System.out.println("Enter source and destinaion for "+ i + "  edge \n");
   int source=sc.nextInt();
   int destination=sc.nextInt();
   
   ver[i][0]=source;
   ver[i][1]=destination;
   
   graph.addedge(source, destination);
  }

  for(int i=0;i<e;i++) 
  {
	  gra[ver[i][0]][ver[i][1]]=1;
	  gra[ver[i][1]][ver[i][0]]=1;
  }
	System.out.println("  Adjacency Matrix \n \n");
  for(int i=0;i<v;i++) {
	  for(int j=0;j<v;j++) {
		  System.out.print(gra[i][j]+" ");
	  }
	  System.out.println();
  }
  
  System.out.println("\n \n Adjacency List\n \n");
  int count=0;
  for(LinkedList l : graph.adj) {
   System.out.println("Linked List "+ (count++)+ " -> " +l);
  }
   
   
  

 }

}
