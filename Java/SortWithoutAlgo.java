public class SortWithoutAlgo {

  public static void main(String[] args) {

    int array[] = {1, 0, 2, 0, 1, 1, 2, 0, 0, 2, 1, 1};
    // simpleSort(array);
    dutchNationalFlag(array);
  }

  /*
   * Time Complexity - O(n)
   * Space Complexity -  O(1)
   */
  private static void dutchNationalFlag(int[] array) {
    // TODO Auto-generated method stub
    int low = 0;
    int mid = 0;
    int temp;
    int high = array.length - 1;

    while (mid <= high) {

      switch (array[mid]) {
      case 0: {
        temp = array[low];
        array[low] = array[mid];
        array[mid] = temp;
        low++;
        mid++;
        break;
      }
      case 1: {
        mid++;
        break;
      }
      case 2: {
        temp = array[high];
        array[high] = array[mid];
        array[mid] = temp;
        high--;
        break;
      }
      }
    }

    for (int i : array) {
      System.out.println(i);
    }
  }

  /*
   * Time Complexity - O(n^2)
   * Space Complexity -  O(1)
   */
  private static void simpleSort(int[] array) {
    // TODO Auto-generated method stub
    for (int i = 0; i < array.length; i++) {
      for (int j = i + 1; j < array.length; j++) {
        if (array[i] > array[j]) {
          int temp = array[i];
          array[i] = array[j];
          array[j] = temp;
        }
      }
    }

    for (int i : array) {
      System.out.println(i);
    }
  }
}
