using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class LogicScript : MonoBehaviour
{
    public GameObject Button;
    public GameObject particle;
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
}
