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
	return (new);
}
