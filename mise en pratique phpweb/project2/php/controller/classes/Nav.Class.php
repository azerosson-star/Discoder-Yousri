<?php


class Navbar {
    private array $liens;

    public function __construct(array $liens) {
        $this->liens = $liens;
    }

    
    public function genererHTML(): string {
        $html = "";
        foreach ($this->liens as $url => $label) {
            $html .= "<a href='$url' class='td-none'>$label</a>\n";
        }
        return $html;
    }
}