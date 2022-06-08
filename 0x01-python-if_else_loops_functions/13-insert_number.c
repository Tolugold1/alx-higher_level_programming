#include "lists.h"
#include <stdlib.h>

/**
* insert_node - function to insert node
* @head: pointer to the head node
* @number: data of the new node
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;
<<<<<<< HEAD
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	while (current != NULL)
	{
		if (current->n < new->n)
		{
			current->next = new;
			new = current->next;
		}
		current->next = new;
	}
=======
	if (!head)
		return NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (number < current->n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next)
		{
			if (number > current->next->n)
				current = current->next;
			else
				break;
		}
		new->next = current->next;
		current->next = new;
	}

>>>>>>> 149c3f2550ea6e3f3d5d9d94b581274ea0fd052d
	return (new);
}
