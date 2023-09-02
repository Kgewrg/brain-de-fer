using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using Unity.VisualScripting;


public class Sliderscript : MonoBehaviour
{
    public Slider mainslider;
    public Slider focusBar;
    public LogicScript logic;
    private float player1,starttime,endtime,Finaltime,player2,maxValue;
    private string row,filePath;
    private bool gameover;
    private int gameMode;

    static public float publicSliderValue;    

    public pauseMenuScript pauseMenu;



    // Start is called before the first frame update
    void Start()
    {
        starttime=Time.time;
        gameover=false;
        maxValue=mainslider.maxValue;
        mainslider.value=maxValue/2;
        publicSliderValue = mainslider.value;
        filePath="C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\data.csv";
        // filePath="C:\\Users\\Dounas P\\Desktop\\brain-de-fair\\data.csv";//βάλτο σε σχόλιο όταν δεν το χρησιμοποιείς

        focusBar.gameObject.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        if(gameover == false) 
        {
            try
            {
                // Read value from csv
                string[] lines = File.ReadAllLines(filePath);//χωρίζω το csv σε ενα πίνακα που κάθε στήλη είναι ένας αριθμός(ποσοστό)
                lines=lines[0].Split(',');                  

                player1 = float.Parse(lines[0]);
                UserInterfaceSricpt.P1_EggConStatus = int.Parse(lines[2]);

                // Check για game mode και δυσκολία
                int gameMode = PlayerPrefs.GetInt("gameMode", -1);
                if (gameMode == 0){
                    focusBar.gameObject.SetActive(false);
                    player2 = float.Parse(lines[1]);
                }                
                else if (gameMode == 1){
                    focusBar.gameObject.SetActive(true);
                    focusBar.value = player1/100;
                    player2 = Bot(PlayerPrefs.GetInt("botDifficulty", -1)) * int.Parse(lines[2]);
                }
                else {
                    Debug.LogError("Error while fetching game mode");
                }
                // Debug.Log("Current value of player1 : "+ player1+" Value of Player2 : "+player2);
                
                if( player1 > player2 )
                {
                    mainslider.value = mainslider.value + Time.deltaTime;
                    publicSliderValue = mainslider.value;
    
                }
                else if(player1 < player2)
                {
                    mainslider.value = mainslider.value - Time.deltaTime;
                    publicSliderValue = mainslider.value;
                }
            }
            catch (IOException){
                // Debug.Log("File was opened, skipping");
            }
            if( mainslider.value == mainslider.maxValue )
            {
                gameover = logic.GameOverPlayer("Player 1 wins");
                endtime=Time.time;
                Finaltime=starttime-endtime;
                
            }
            else if ( mainslider.value == mainslider.minValue)
            {
                gameover = logic.GameOverPlayer("Player 2 wins");
                endtime=Time.time;
                Finaltime=starttime-endtime;
            }

        }
    }

    float Bot(int difficultyLevel){
        int min, max;

        if (difficultyLevel == 0){ // Easy
            min = 30;
            max = 100;
        }
        else if (difficultyLevel == 1){ // Normal
            min = 50;
            max = 100;
        }
        else if (difficultyLevel == 2){ // Hard
            min = 70;
            max = 100;
        }
        else { 
            // Για την περίπτωση που δεν μπεί σωστή τιμή, παίζει στο esay
            // Πιο σωστό θα ήταν να έβγαζε error, αλλα είναι λίγο περίπλοκο 
            // να διαχειριστεί και δεν θα συμβαίνει εκτως development
            Debug.LogWarning("sliderScript: Wrong difficulty value, playing on easy");
            
            min = 30;
            max = 100;
             
        }

        return Random.Range(min, max);

    }
    
}

