using TMPro;
using Unity.VisualScripting;
using UnityEngine;

public class LogicScript : MonoBehaviour
{
    public GameObject gameOverPanel;
    public pauseMenuScript pauseMenu;

    void Start(){
        pauseMenu = GameObject.FindGameObjectWithTag("pauseTag").GetComponent<pauseMenuScript>();
    }
    
    public bool GameOverPlayer(string message) {
        Time.timeScale = 0f;
        gameOverPanel.SetActive(true);
        
        // βαζει το text
        TMP_Text winnerTextBox = gameOverPanel.GetComponentInChildren<TMP_Text>();
        winnerTextBox.text = message;

        return true;
    }

    public void button(){
        pauseMenu.RestartGame();
    }



    void Update() {
   
    }
}
