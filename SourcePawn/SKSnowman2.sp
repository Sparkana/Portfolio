#pragma semicolon 1

#define DEBUG

#define PLUGIN_AUTHOR "Sparkana"
#define PLUGIN_VERSION "1.10"

#include <sourcemod>
#include <sdktools>
#include <tf2>
#include <tf2_stocks>
//#include <SKInclude>
//#include <clients>
//#include <sdkhooks>

public Plugin myinfo = 
{
	name = "Snowman",
	author = PLUGIN_AUTHOR,
	description = "Snowman death messages",
	version = PLUGIN_VERSION,
	url = ""
};

int snowman_clientindex = -1;
int snowman_killcount = 0;

public void OnPluginStart() {
	HookEvent("player_death", Event_PlayerDeath, EventHookMode_Pre);
}

public void OnMapStart() {
	snowman_clientindex = -1;
}

public Action Event_PlayerDeath(Event event, const char[] name, bool dontBroadcast) {
	
	//Variables
	int x;
	//PrintToChatAll("ClientIndex #: %d", snowman_clientindex); //Debug
	
	if (event.GetInt("assister") == -1 && snowman_clientindex != -1) {
		event.SetInt("assister", GetClientUserId(snowman_clientindex));
		snowman_killcount++;
	}
	
	if (snowman_clientindex == -1) {
		x = GetRandomInt(1, 10);
		//PrintToChatAll("Rand #: %d", x); //Debug
		if (x > 5) {
			snowman_clientindex = CreateFakeClient("SNOWMAN");
			PrintToChatAll("The SNOWMAN has arrived!");
		}
	}
	
	if (snowman_killcount > 0 && snowman_killcount % 5 == 0) {
		PrintToChatAll("Snowman kill counter: %d", snowman_killcount);
	}
	
	return Plugin_Continue;
}
