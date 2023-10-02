#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @x: list
 *
 * Return: 1
 */
int check_cycle(listint_t *x)
{
	listint_t *s = x;
	listint_t *f = x;

	if (!x)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}
