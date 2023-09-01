using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class pauseMenuScript : MonoBehaviour
{
    public static bool pauseFlag = false;

    public GameObject pauseMenu;
    public GameObject optionsMenu;
    public TMP_Dropdown gameModeDropdown;
    public TMP_Dropdown difficultyDropdown;


    void Start(){
        // Παίρνει τις ρυθμίσεις απο το main manu και τις βάζει στο pause menu
        gameModeDropdown.value = PlayerPrefs.GetInt("gameMode", -1);
        difficultyDropdown.value = PlayerPrefs.GetInt("botDifficulty", -1);
    }

    // Update is called once per frame
    void Update() {
        if (Input.GetKeyDown(KeyCode.Escape)){
            if (pauseFlag == true){ // το παιχνίδι είναι pause
                resume();
            }
            else {
                pause();
            }
        }   
    }

    public void resume(){
        pauseMenu.SetActive(false);
        optionsMenu.SetActive(false);
        Time.timeScale = 1f;
        pauseFlag = false;
    }
    void pause(){
        pauseMenu.SetActive(true);
        Time.timeScale = 0f;
        pauseFlag = true;
    }

    public void BotDifficulty(int difficultyIndex){
        // difficultyIndex: 0 Easy, 1 Medium, 2 Hard
        // --> Needs Testing
        PlayerPrefs.SetInt("botDifficulty", difficultyIndex);

    }

    public void GameMode(int gameModeIndex){
        // gameModeValue: 0 PvP, 1 PvE
        // --> Needs Testing
        PlayerPrefs.SetInt("gameMode", gameModeIndex);
    }

    public void QuitGame()
    {   
        Debug.Log("Quit!");
        Application.Quit();
    }
    public void restartGame()
    {
        resume();
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }


}
