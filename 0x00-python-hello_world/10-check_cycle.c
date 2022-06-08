<<<<<<< HEAD
#include "list.h"
#include <stdio.h>

=======
#include <stdio.h>
#include "lists.h"  
>>>>>>> 149c3f2550ea6e3f3d5d9d94b581274ea0fd052d
/**
 * check_cycle - function to check for presence of curcle
 * in sigly linked list
 * @list: node pointer
 * Return: 0 if there's no circle otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *node;
<<<<<<< HEAD

	node = list;
	while (node)
	{
		list = list->next;
		if (list->next == node)
			return (1);
	}
	return (0);
}

=======
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
>>>>>>> 149c3f2550ea6e3f3d5d9d94b581274ea0fd052d
