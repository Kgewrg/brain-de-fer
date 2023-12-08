using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using TMPro;
using System;

public class MainMenu : MonoBehaviour
{

    public TMP_Text outputTextBox;
    public void Start(){
        // For the first start of the game 
        PlayerPrefs.SetInt("botDifficulty", 0);
        PlayerPrefs.SetInt("gameMode", 0);
        PlayerPrefs.SetInt("classifier", 0);
    }
    public void PlayGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }
    
    public void QuitGame()
    {   
        UnityEngine.Debug.Log("Quit!");
        Application.Quit();
    }

    public void BotDifficulty(int difficultyIndex){
        // difficultyIndex: 0 Easy, 1 Medium, 2 Hard
        PlayerPrefs.SetInt("botDifficulty", difficultyIndex);
    }

    public void GameMode(int gameModeIndex){
        // gameModeValue: 0 PvP, 1 PvE
        PlayerPrefs.SetInt("gameMode", gameModeIndex);
    }

    public void classifierSelector(int classifierIndex){
        PlayerPrefs.SetInt("classifier", classifierIndex);
    }



    public void startBridge(){
        string dirPath = Application.dataPath;
        string dataFilePath = Path.Combine(dirPath, "data.csv");

        if (! File.Exists(dataFilePath)){
            Debug.LogError("Could not find data file");
            outputTextBox.SetText("Could not find data file");
        } 

        outputTextBox.SetText(File.ReadAllLines(dataFilePath)[0]);
    }
}
