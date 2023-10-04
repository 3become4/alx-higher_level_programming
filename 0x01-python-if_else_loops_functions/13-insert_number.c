#include "lists.h"

/**
 * insert_node - Write a function in C that inserts a number into a sorted singly linked list.
 *
 * @head: head
 * @number: number
 *
 * Return: pointer to node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x = *head, *y;

	y = malloc(sizeof(listint_t));
	if (y == NULL)
		return (NULL);
	y->n = number;

	if (x == NULL || x->n >= number)
	{
		y->next = x;
		*head = y;
		return (y);
	}

	while (x && x->next && x->next->n < number)
		x = x->next;

	y->next = x->next;
	x->next = y;

	return (y);
}
