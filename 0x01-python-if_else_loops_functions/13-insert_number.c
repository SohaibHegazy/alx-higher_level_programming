#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function to insert node in linked list
 * @head: pointer to the head of the list
 * @number: the number to be inserted in new node
 *
 * Return: pointer to the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!current || number < current->n)
	{
		new->next = current;
		*head = new;
		return (*head);
	}

	while(current)
	{
		if (number < current->next-> || !current->next)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current  = current->next;
	}
	return (NULL);
}
