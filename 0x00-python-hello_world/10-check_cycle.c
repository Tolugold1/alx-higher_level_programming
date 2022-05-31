#include <stdio.h>
#include "lists.h"  
/**
 * check_cycle - function to check for presence of curcle
 * in sigly linked list
 * @list: node pointer
 * Return: 0 if there's no circle otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *node;
	listint_t *temp;

	node = list;
	temp = list;
	while (node && temp && temp->next)
	{
		node = node->next;
		temp = temp->next->next;
		if (node == temp)
			return (1);
	}
        return (0);
}
