using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;



public class Sliderscript : MonoBehaviour
{
    public Slider mainslider;
    public Slider focusBar;
    public LogicScript logic;
    public static float player1, player2;
    private float starttime,endtime,Finaltime,maxValue;
    private string row,filePath;
    private bool gameover;
    private int gameMode;

    static public float publicSliderValue;    

    public pauseMenuScript pauseMenu;

    private string leftPlayerGameOverText; 
    private string rightPlayerGameOverText; 

    // Πόσες τιμες να σκιπαρει πριν αρχίσει να μετράει score
    private int skipCounter = 3; 
    private float player1_previous;

    // Variables for checking if the attention values are updating in game
    private int failedToUpdateCounter = 2;
    private float localPlayer1_previous = 0;    
    private float localPlayer2_previous = 0;


    void Start()
    {
        starttime=Time.time;
        gameover=false;
        maxValue=mainslider.maxValue;
        mainslider.value=maxValue/2;
        publicSliderValue = mainslider.value;
        filePath = Path.Combine(Application.dataPath, "data.csv"); // Το data path ειναι στα assets τωρα πια, για λόγους μετα του build

        if (! File.Exists(filePath)){
            Debug.LogError("Could not find data file");
        } 
        focusBar.gameObject.SetActive(false);
        player1 = player1_previous = 0;
        


        InvokeRepeating("checkIfValuesUpdated", 0f, 1f); // Calls this func every second
    }


    void Update()
    {
        if(gameover == false) 
        {
            try
            {
                // Read value from csv
                string[] lines = File.ReadAllLines(filePath); //χωρίζω το csv σε ενα πίνακα που κάθε στήλη είναι ένας αριθμός(ποσοστό)
                lines=lines[0].Split(',');                  

                player1_previous = player1;
                player1 = float.Parse(lines[0]);
                
                // Change detector
                if ((player1_previous != player1) && (skipCounter > 0)){
                    skipCounter -= 1; 
                }
                
                // Δεν επιτρέπει να τρέξει όσο το counter δεν έχε τελειώσει
                if (skipCounter > 0){
                    return;
                }
                

                // Ενημερώνει για την κατάταση της σύνδεσης της συκευής
                UserInterfaceSricpt.P1_EggConStatus = int.Parse(lines[2]);

                // Check για game mode και δυσκολία
                gameMode = PlayerPrefs.GetInt("gameMode", -1);
                if (gameMode == 0){
                    // Παίχτης vs Παίχτης
                    focusBar.gameObject.SetActive(false);                    
                    // player2_previous = player2;
                    player2 = float.Parse(lines[1]);

                                             

                }                
                else if (gameMode == 1){
                    // Παίχτης vs Υπολογιστής
                    focusBar.gameObject.SetActive(true);
                    focusBar.value = player1/100;
                    player2 = Bot(PlayerPrefs.GetInt("botDifficulty", -1)) * int.Parse(lines[2]);
      
                }
                else {
                    Debug.LogError("Error while fetching game mode");
                }
                // Debug.Log("Poor left : "+int.Parse(lines[4])+" Value of Player2 : "+int.Parse(lines[5]));
                
                // Υπολογισμός του score και δημοσίευσή του 
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

            // Αλλαγή του μυνήματος με βάση το gamemode 
            if (PlayerPrefs.GetInt("gameMode", -1) == 0){
                leftPlayerGameOverText = "Left player wins!";
                rightPlayerGameOverText = "Right player wins!";
            } else {
                leftPlayerGameOverText = "Player wins!";
                rightPlayerGameOverText = "Bot wins!";
            }


            // Έλεγχος τερματισμού του παιχνιδιού
            if( mainslider.value == mainslider.maxValue )
            {
                gameover = logic.GameOverPlayer(leftPlayerGameOverText);
                endtime=Time.time;
                Finaltime=starttime-endtime;
                Debug.Log(Finaltime);                
            }
            else if ( mainslider.value == mainslider.minValue)
            {
                gameover = logic.GameOverPlayer(rightPlayerGameOverText);
                endtime=Time.time;
                Finaltime=starttime-endtime;
                Debug.Log(Finaltime);                
            }
        }
    }
    
    void checkIfValuesUpdated(){
        // Checks if the attention values did not update
        
        // Debug.Log("left player:" + localPlayer1_previous + " " + player1);
        // Debug.Log("right player:" + localPlayer2_previous + " " + player2);
        if (skipCounter > 0){
            return;
        }
        
        if ((localPlayer1_previous == player1) || (localPlayer2_previous == player2)){
            failedToUpdateCounter -= 1;
        }
        else { 
            failedToUpdateCounter = 2; 
            UserInterfaceSricpt.DevicesDisconected = false;
        }
        
        if (failedToUpdateCounter <= 0){
            // Debug.LogError("Attention Values are not updating");
            UserInterfaceSricpt.DevicesDisconected = true;
        }

        localPlayer1_previous = player1;
        localPlayer2_previous = player2;

    }


    float Bot(int difficultyLevel){
        // Ρύθμισεις δυσκολίας του bot
        int min, max;

        if (difficultyLevel == 0){ // Easy
            min = 30;
            max = 70;
        }
        else if (difficultyLevel == 1){ // Normal
            min = 40;
            max = 80;
        }
        else if (difficultyLevel == 2){ // Hard
            min = 60;
            max = 100;
        }
        else { 
            // Για την περίπτωση που δεν μπεί σωστή τιμή, παίζει στο easy
            // Πιο σωστό θα ήταν να έβγαζε error, αλλα είναι λίγο περίπλοκο 
            // να διαχειριστεί και δεν θα συμβαίνει εκτως development
            Debug.LogWarning("sliderScript: Wrong difficulty value, playing on easy");
            
            min = 30;
            max = 70;
             
        }

        return Random.Range(min, max);

    }
    
}

