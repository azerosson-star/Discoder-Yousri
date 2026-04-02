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

	static function getHost()
	{
		return self::$_host;
	}

	static function getPort()
	{
		return self::$_port;
	}

	static function getDbname()
	{
		return self::$_dbname;
	}

	static function getLogin()
	{
		return self::$_login;
	}

	static function getPwd()
	{
		return self::$_pwd;
	}
	#endregion
	static function init()
	{
		if (file_exists("config.json")) {

			$parametre  = json_decode(file_get_contents("config.json"));
			self::$_nomProjet = $parametre->NomProjet;
			self::$_host = decode($parametre->Host);
			self::$_port = $parametre->Port;
			self::$_dbname = decode($parametre->DbName);
			self::$_login = decode($parametre->Login);
			if (strlen($parametre->Pwd) == 0)
				self::$_pwd = $parametre->Pwd; //developpement
			else
				self::$_pwd = decode($parametre->Pwd); //production
		}
	}
}