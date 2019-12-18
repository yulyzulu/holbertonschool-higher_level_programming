#include "lists.h"
/**
*is_palindrome- function that checks if a singly list is a palindrome
*@head: listin_t double pointer
*Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp1;
	int list1[10000];
	int i, j;

	temp1 = *head;
	i = 0;
	while (temp1)
	{
		list1[i] = temp1->n;
		temp1 = temp1->next;
		i++;
	}
	if (i == 1)
	{
		return (1);
	}
	else
	{
		i--;
		for (j = 0; j < i; j++)
		{
			if (list1[i] != list1[j])
				return (0);
			i--;
		}
	}
	return (1);
}
