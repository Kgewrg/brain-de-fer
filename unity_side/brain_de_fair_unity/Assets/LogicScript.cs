using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class LogicScript : MonoBehaviour
{
    public GameObject optionsMenu;
    public GameObject Button;
    public GameObject particle;

    private int inMenu = 0; // 1 οταν είναι στο menu
    public void restartGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
    
    public bool GameOverPlayer(string message)
    {   
        
        Text buttonText = Button.GetComponentInChildren<Text>();
        buttonText.text=message;
        Button.SetActive(true);
        particle.GetComponent<ParticleSystem>().Stop();
        return true;
    }

    void Update() {
        // If escape is pressed, make the game object active
        if (Input.GetKeyDown(KeyCode.Escape)){
            if (inMenu == 0){
                SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex - 1);
                inMenu = 1;
            }
            else if (inMenu == 1){
                SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
                inMenu = 0;
            }
        }
    }
}
