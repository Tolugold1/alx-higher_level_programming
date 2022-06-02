#include "list.h"
#include <stdio.h>

/**
 * check_cycle - function to check for presence of curcle
 * in sigly linked list
 * @list: node pointer
 * Return: 0 if there's no circle otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *node;

	node = list;
	while (node)
	{
		list = list->next;
		if (list->next == node)
			return (1);
	}
	return (0);
}

