using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class UserInterfaceSricpt : MonoBehaviour
{
    public static int P1_EggConStatus;
    public GameObject conStatusMessage_container;
    // public TMP_Text P2_EGG_text;
    public static bool DevicesDisconected = false;
    public GameObject DevDC_container;


    public TMP_Text rightPlayerTextbox;
    public TMP_Text leftPlayerTextbox;

    public Slider LeftPlayerHealth;
    public Slider RightPlayerHealth;

    private float sliderValue;

    void Start() {
        conStatusMessage_container.SetActive(false);
    }

    void Update() {

        // Αν δεν έχει συνδεθεί η συσκευή, εμφανίζει το text
        if (P1_EggConStatus == 0){
            conStatusMessage_container.SetActive(true);
        }else{
            conStatusMessage_container.SetActive(false);
        }

        if (DevicesDisconected == true){
            DevDC_container.SetActive(true);

        }else {
            DevDC_container.SetActive(false);
        }



        // Gia 2 paixtes
        // if ((P1_EggConStatus == 0) || P2_EggConStatus == 0){
        //     conStatusMessage_container.SetActive(true);
        // }else{
        //     conStatusMessage_container.SetActive(false);

        // }


        if (PlayerPrefs.GetInt("gameMode", -1) == 1){
            rightPlayerTextbox.SetText("Bot's health");
            leftPlayerTextbox.SetText("Player's health");
        }
        else {
            rightPlayerTextbox.SetText("right player's health");
            leftPlayerTextbox.SetText("Left player's health");
        }

        sliderValue = Sliderscript.publicSliderValue - 5;
        LeftPlayerHealth.value = Remap(sliderValue, 0, -5, 0, 1);
        RightPlayerHealth.value = Remap(sliderValue, 0, 5, 0, 1); 

                      
    }

    float Remap (float value, float from1, float to1, float from2, float to2) {
        return (value - from1) / (to1 - from1) * (to2 - from2) + from2;
    }
}
