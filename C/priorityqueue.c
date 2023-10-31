#include <stdio.h>
#include <stdlib.h>

typedef struct priority_queue {
  int *data;
  int size;
  int capacity;
} PriorityQueue;

PriorityQueue *create_priority_queue(int capacity) {
  PriorityQueue *queue = malloc(sizeof(PriorityQueue));
  queue->data = malloc(sizeof(int) * capacity);
  queue->size = 0;
  queue->capacity = capacity;
  return queue;
}

void enqueue(PriorityQueue *queue, int element) {
  if (queue->size == queue->capacity) {
    printf("Priority queue is full.\n");
    return;
  }

  int i = queue->size;
  queue->data[i] = element;
  queue->size++;

  // Maintain the priority queue by sifting up the element.
  while (i > 0) {
    int parent_index = (i - 1) / 2;
    if (queue->data[i] > queue->data[parent_index]) {
      int temp = queue->data[i];
      queue->data[i] = queue->data[parent_index];
      queue->data[parent_index] = temp;
      i = parent_index;
    } else {
      break;
    }
  }
}

int dequeue(PriorityQueue *queue) {
  if (queue->size == 0) {
    printf("Priority queue is empty.\n");
    return -1;
  }

  int element = queue->data[0];
  queue->size--;

  // Move the last element to the root
  queue->data[0] = queue->data[queue->size];

  // Maintain the priority queue by sifting down the element.
  int i = 0;
  while (1) {
    int left_child_index = 2 * i + 1;
    int right_child_index = 2 * i + 2;
    int largest = i;

    if (left_child_index < queue->size && queue->data[left_child_index] > queue->data[largest]) {
      largest = left_child_index;
    }

    if (right_child_index < queue->size && queue->data[right_child_index] > queue->data[largest]) {
      largest = right_child_index;
    }

    if (largest != i) {
      int temp = queue->data[i];
      queue->data[i] = queue->data[largest];
      queue->data[largest] = temp;
      i = largest;
    } else {
      break;
    }
  }

  return element;
}

int main() {
  PriorityQueue *queue = create_priority_queue(5);

  enqueue(queue, 10);
  enqueue(queue, 20);
  enqueue(queue, 30);
  enqueue(queue, 40);

  printf("Dequeued element: %d\n", dequeue(queue));
  printf("Dequeued element: %d\n", dequeue(queue));

  return 0;
}
