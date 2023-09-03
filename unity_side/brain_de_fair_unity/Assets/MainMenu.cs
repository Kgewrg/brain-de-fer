using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    
    

    public void PlayGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }
    
    public void QuitGame()
    {   
        Debug.Log("Quit!");
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
}
