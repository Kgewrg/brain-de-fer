using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{

    static public int publicDifficultyLevel;    
    static public int publicGameMode;

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
        publicDifficultyLevel = difficultyIndex;
    }

    public void GameMode(int gameModeValue){
        // gameModeValue: 0 PvP, 1 PvE
        publicGameMode = gameModeValue;


    }
}
