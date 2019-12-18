#include "lists.h"
/**
*is_palindrome- function that checks if a singly list is a palindrome
*@head: listin_t double pointer
*Return: 0 if it is not a palindrome, 1 if it is a palindrome
*
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp1, *temp2;
	unsigned int i, j;

	temp1 = *head;
	temp2 = *head;
	i = 0;
	while (temp1 && temp1->next)
	{
		temp1 = temp1->next;
		i++;
	}
	i = i / 2;
	temp1 = *head;
	for (j = 0; j < i; j++)
	{
		temp1 = temp1->next;
	}
	if (temp1->next == temp2->next)
		return (1);
	return (0);
}
