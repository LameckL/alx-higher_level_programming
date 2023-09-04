#include "lists.h"

/**
 * check_cycle - this funtion checks if a singly
 * linked list has a cycle in it
 * @list: the singly linked list
 * Return: 0 - no cycle, 1 - there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}