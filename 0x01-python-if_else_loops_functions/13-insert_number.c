#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
*insert_node- function that insert new node into a sorted singly linked list
*@head: double pointer listint
*@number: integer
*Return: the address of the new node or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *point1, *point2, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	point1 = *head;
	new_node->n = number;
	if (new_mode->number < point1->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

return (new_node);
}
