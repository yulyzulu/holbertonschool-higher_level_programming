#include "lists.h"
/**
*check_cycle- check if a singly linked list has a cycle in it 
*@list: listint_t pointer
*Return: 1 cycle, 0 no cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *prox;

	current = list;
	prox = list;
	
	while (current && prox && prox->next)
	{
		current = current->next;
		prox = prox->next->next;

		if (current == prox)
		{
			return (1);

		}
	}
	return (0);
}
