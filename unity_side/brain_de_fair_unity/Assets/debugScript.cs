using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using TMPro;
using UnityEngine;

public class debugScript : MonoBehaviour
{
    public GameObject debugPanel;
    private bool debguIsVisible = false;

    public TMP_Text gameModeField;
    public int gameMode = -1 ;
    private readonly string[] gameModeStrings = {"pvp", "pve"};

    public TMP_Text difficultyField; 
    public int difficultyLevel = -1;
    private readonly string[] difficultyStrings = {"easy", "medium", "hard"};

    public TMP_Text classifierField;
    public int cliassifierValue = -1;
    private readonly string[] classifierStrings = {"device", "ML"};
    void Start()
    {
        
    }

    void Update() {
        if (Input.GetKeyDown(KeyCode.D)){
            if (debguIsVisible == true){ // το παιχνίδι είναι pause
                hideDebug();
            }
            else {
                showDebug();
            }
        }
        
        gameMode = PlayerPrefs.GetInt("gameMode", -1); 
        gameModeField.SetText(gameMode + "("+gameModeStrings[gameMode]+")");

        difficultyLevel = PlayerPrefs.GetInt("botDifficulty", -1);
        difficultyField.SetText(difficultyLevel + "("+difficultyStrings[difficultyLevel]+")");

        cliassifierValue = PlayerPrefs.GetInt("classifier", -1);
        classifierField.SetText(cliassifierValue + "("+classifierStrings[cliassifierValue]+")");
    }
    void showDebug(){
        debugPanel.SetActive(true);
        debguIsVisible=true;
    }
    void hideDebug(){
        debugPanel.SetActive(false);
        debguIsVisible=false;
    }
}
