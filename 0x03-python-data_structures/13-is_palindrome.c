#include "lists.h"

listint_t *reverse_listint(listint_t **x);
int is_palindrome(listint_t **x);

/**
 * reverse_listint - Reverses list.
 *
 * @x: start of list
 *
 * Return: reversed list
 */
listint_t *reverse_listint(listint_t **x)
{
	listint_t *y = *x, *next, *prev = NULL;

	while (y)
	{
		next = y->next;
		y->next = prev;
		prev = y;
		y = next;
	}

	*x = prev;
	return (*x);
}

/**
 * is_palindrome - if is palindrome.
 *
 * @x: start of list
 *
 * Return: 0 or 1
 */
int is_palindrome(listint_t **x)
{
	listint_t *tmp, *rev, *mid;
	size_t s = 0, i;

	if (*x == NULL || (*x)->next == NULL)
		return (1);

	tmp = *x;
	while (tmp)
	{
		s++;
		tmp = tmp->next;
	}

	tmp = *x;
	for (i = 0; i < (s / 2) - 1; i++)
		tmp = tmp->next;

	if ((s % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *x;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}

