#pragma semicolon 1

#define DEBUG

#define PLUGIN_AUTHOR "Sparkana"
#define PLUGIN_VERSION "1.00"

#include <sourcemod>
#include <sdktools>
#include <tf2>
#include <tf2_stocks>
//#include <sdkhooks>

public Plugin myinfo = 
{
	name = "Chat calculator",
	author = PLUGIN_AUTHOR,
	description = "Chat calculator",
	version = PLUGIN_VERSION,
	url = ""
};

public void OnPluginStart()
{
	RegConsoleCmd("sm_skdouble", Command_skDouble, "Doubles a number");
	RegConsoleCmd("double", Command_skDouble, "Doubles a number");
	RegConsoleCmd("calc", Command_skCalculate, "Does basic mathematial calculations");
}

public Action OnClientCommand(int client, int args) {
	//PrintToChat(client, "Command called");
	return Plugin_Continue;
}

public Action Command_skDouble(int client, int args) {
	int num; 
	char arg1[32];
	GetCmdArg(1, arg1, sizeof(arg1));
	num = StringToInt(arg1, 10);
	
	PrintToChat(client, "%d * 2 = %d", num, num * 2);
	return Plugin_Continue;
}

public Action Command_skCalculate(int client, int args) {
	//char[][] operators = new char[(args - 1) / 2][2];
	ArrayList operators = new ArrayList();
	ArrayList numbers = new ArrayList();
	int total = 0;
	
	for (int i = 1; i <= args; i++) {
		char argBuffer[32];
		GetCmdArg(i, argBuffer, sizeof(argBuffer));
		if (i % 2 == 1) {
			numbers.Push(StringToInt(argBuffer));
		}
		else if (i % 2 == 0) {
			operators.PushString(argBuffer);
		}
	}
	
	int num1 = 0;
	int num2 = 0;
	int currentOp = -1;
	
	//Check for multiplication
	while (operators.FindString("*") != -1) {
		//Find next multiplication step
		currentOp = operators.FindString("*");
		
		//Get numbers to multiply
		num1 = numbers.Get(currentOp);
		num2 = numbers.Get(currentOp + 1);
		
		//Set the first value to the product
		numbers.Set(currentOp, num1 * num2);
		
		//Remove the other indexes to simplify the calculation
		operators.Erase(currentOp);
		numbers.Erase(currentOp + 1);
	}
	
	//Check for subtraction
	while (operators.FindString("-") != -1) {
		//Find next subtraction step
		currentOp = operators.FindString("-");
		
		//Get numbers to subtract
		num1 = numbers.Get(currentOp);
		num2 = numbers.Get(currentOp + 1);
		
		//Set the first value to the difference
		numbers.Set(currentOp, num1 - num2);
		
		//Remove the other indexes to simplify the calculation
		operators.Erase(currentOp);
		numbers.Erase(currentOp + 1);
	}
	
	//Check for addition
	while (operators.FindString("+") != -1) {
		//Find next addition step
		currentOp = operators.FindString("+");
		
		//Get numbers to add
		num1 = numbers.Get(currentOp);
		num2 = numbers.Get(currentOp + 1);
		
		//Set the first value to the total
		numbers.Set(currentOp, num1 + num2);
		
		//Remove the other indexes to simplify the calculation
		operators.Erase(currentOp);
		numbers.Erase(currentOp + 1);
	}
	
	total = numbers.Get(0);
	
	PrintToChat(client, "Result of input: %d", total);
	return Plugin_Handled;
}