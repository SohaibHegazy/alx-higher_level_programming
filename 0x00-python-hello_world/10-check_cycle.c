#include "lists.h"

/**
 * check_cycle - to check if there is a cycle in the list
 * @list: the pointer to the head of the list
 *
 * Return: 1 if there is a cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *p1 = list, *p2 = list;

	while (p1 && p1->next)
	{
		p2 = p2->next;
		p1 = p1->next->next;
		if (p1 == p2)
			return (1);
	}
	return (0);
}
