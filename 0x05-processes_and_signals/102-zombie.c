#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int infinite_while(void);


/**
 * main - creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t p_id;
	char c = 0;

	while (c < 5)
	{
		p_id = fork();
		if (p_id > 0)
		{
			printf("Zombie process created, PID: %d\n", p_id);
			sleep(1);
			c++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
/**
 * infinite_while - runs an infinite while loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
