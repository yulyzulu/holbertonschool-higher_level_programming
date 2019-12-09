#include "lists.h"
/**
*
*
*
*
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
