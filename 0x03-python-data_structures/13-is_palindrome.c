#include "lists.h"

/**
 * is_palindrome - function to check if linked list is palindrome
 * @head: pointer to head
 *
 * Return: 1 if true and 0 if false
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (pal(head, *head));
}

/**
 * pal - the function
 * @head: pointer to head
 * @end: pointer to end
 *
 * Return: 1 if true and 0 if false
 */

int pal(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (pal(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
