#pragma semicolon 1

#define DEBUG

#define PLUGIN_AUTHOR ""
#define PLUGIN_VERSION "0.00"

#include <sourcemod>
#include <sdktools>
#include <tf2>
#include <tf2_stocks>
//#include <sdkhooks>

public Plugin myinfo = 
{
	name = "skTest",
	author = "Spark",
	description = "Command test",
	version = "1.0",
	url = ""
};

ConVar sm_skslap_damage = null;

public void OnPluginStart()
{
	RegAdminCmd("sm_skslap", Command_skSlap, ADMFLAG_SLAY);
	
	sm_skslap_damage = CreateConVar("sm_skslap_damage", "5", "Default slap damage");
	AutoExecConfig(true, "plugin_skslap");
}

public Action Command_skSlap(int client, int args) {
	//Variables
	int damage = GetConVarInt(sm_skslap_damage);
	char arg1[32], arg2[32];
	
	GetCmdArg(1, arg1, sizeof(arg1));
	
	if (args >= 2) {
		GetCmdArg(2, arg2, sizeof(arg2));
		damage = StringToInt(arg2);
	}
	
	int target = FindTarget(client, arg1);
	if (target == -1) {
		return Plugin_Handled;
	}
	
	SlapPlayer(target, damage);
	
	char name[MAX_NAME_LENGTH];
	
	GetClientName(target, name, sizeof(name));
	
	ShowActivity2(client, "[SM] ", "Slapped %s for %d damage!", name, damage);
	LogAction(client, target, "\"%L\" slapped \"%L\" (damage %d)", client, target, damage);
	
	return Plugin_Handled;
}