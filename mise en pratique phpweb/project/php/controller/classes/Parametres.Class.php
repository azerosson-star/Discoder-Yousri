<?php

class Parametres
{
	private static $_nomProjet;
	private static $_host;
	private static $_port;
	private static $_dbname;
	private static $_login;
	private static $_pwd;

	#region
	static public function getNomProjet()
	{
		return self::$_nomProjet;
	}

	static public function getHost()
	{
		return self::$_host;
	}

	static public function getPort()
	{
		return self::$_port;
	}

	static public function getDbname()
	{
		return self::$_dbname;
	}

	static public function getLogin()
	{
		return self::$_login;
	}

	static public function getPwd()
	{
		return self::$_pwd;
	}
	#endregion
	static public function init()
	{
		if (file_exists("config.json")) {

			$parametre  = json_decode(file_get_contents("config.json"));
			self::$_nomProjet = $parametre->NomProjet;
			self::$_host = $parametre->Host;
			self::$_port = $parametre->Port;
			self::$_dbname = $parametre->DbName;
			self::$_login = $parametre->Login;
			if (strlen($parametre->Pwd) == 0)
				self::$_pwd = $parametre->Pwd; //developpement
			else
				self::$_pwd = $parametre->Pwd; //production
		}
	}
}