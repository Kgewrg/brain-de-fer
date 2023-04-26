using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class Sliderscript : MonoBehaviour
{
    public Slider mainslider;
    private float maxValue;
    private string filePath;
    private float player1;
    private float player2;
    private string row;
    // Start is called before the first frame update
    void Start()
    {
       maxValue=mainslider.maxValue;
       mainslider.value=maxValue/2;
       filePath="C:\\Users\\Dounas P\\Desktop\\brain-de-fer\\data.csv";//βάλτο σε σχόλιο όταν το χρησιμοποιείς
    }

    // Update is called once per frame
    void Update()
    {
        try{
            string[] lines = File.ReadAllLines(filePath);//χωρίζω το csv σε ενα πίνακα που κάθε στήλη είναι ένας αριθμός(ποσοστό)
            lines=lines[0].Split(',');                  

            player1 = float.Parse(lines[0]);
            player2=float.Parse(lines[1]);
            Debug.Log("Current value of player1 : "+ player1+" Value of Player2 : "+player2);
            
            if( player1 > player2 )
            {
                mainslider.value=mainslider.value+Time.deltaTime;
            }
            else if(player1 < player2)
            {
                mainslider.value=mainslider.value-Time.deltaTime;
            }

        
        }
        catch (IOException){
            Debug.Log("File was opened, skipping");
        }
    }
}
