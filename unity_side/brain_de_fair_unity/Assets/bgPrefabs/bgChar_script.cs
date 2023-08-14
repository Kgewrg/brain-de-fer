using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class bgChar_script : MonoBehaviour
{
    public int totalRandomAnimations = 6;
    public int activeAnim = 0; // Καθορίζει αν θα κάνει κάποιο animation
    public bool teamLeft;  // Καθορίζει σε ποια ομάδα θα είναι (plater1, πρωτη τιμή, [5,10})
    public bool teamRight; // (plater2, Δευτερη τιμή, {0,5])
    public float minInterval = 5;
    public float maxInterval = 10;   
    private Animator mAnimator;

    // Πίνακας που περιέχει τα triggers των animations
    private List<int> hashAvailableAnims = new List<int>(); 

    int winTriggerHash;
    int looseTriggerHash;

    void Start() { 
        mAnimator = GetComponent<Animator>();
        var state = mAnimator.GetCurrentAnimatorStateInfo(0);
        mAnimator.Play(state.fullPathHash, 0 ,Random.Range(0f, 1f));

        // Προσθήκη των hash (id) των trigger στον πίνακα)
        for (int i = 0; i < totalRandomAnimations; i++) {
            hashAvailableAnims.Add(Animator.StringToHash(i.ToString()));
            // Κάνει το index σε string, έτσι ώστε να αντιστοιχεί στο 
            // trigger για κάποιο animation
        }
        
        // Ενα αρχικό random ξεκίνημα έτσι ώστε να μην ξεκινάνε όλα τα idle ταυτόχρονα
        float randInterval = Random.Range(minInterval, maxInterval);
        Invoke("randomlyInvokeAnim", randInterval);
      
    }

    void Update() {
        
        winTriggerHash = Animator.StringToHash("win");
        looseTriggerHash = Animator.StringToHash("loose");

        // Κάνει false όλα τα triggers ωστε να μην παίζουν επαναληπτικά
        foreach (int triggerHash in hashAvailableAnims) {
           mAnimator.SetBool(triggerHash, false);
        }

        mAnimator.SetBool(winTriggerHash, false);
        mAnimator.SetBool(looseTriggerHash, false);



    }

    void randomlyInvokeAnim(){
        // Αυτό καλείτε μια φορά στην αρχή και μετα μάλλον καλείτε απο μόνο του
        // όποτε θέλει ???
        // https://www.youtube.com/watch?v=a76azKiNsYM
        float randInterval = Random.Range(minInterval, maxInterval);
        Invoke("randomlyInvokeAnim", randInterval);
        // Debug.Log("Calling anim");
        playAnim();
    }
    
    void playAnim(){
        // Ελέγχει αν είναι active χαρακτήρας και αν παίζει ήδη κάποιο animation
        float sliderValue = Sliderscript.publicSliderValue;


        if ((activeAnim == 1)){
            // Αν φτάνει κοντα στα άκρα η τιμή τότε παίζει μόνο win/loose animations
            if (sliderValue > 7){
                if (teamLeft) { // [5,10}
                    mAnimator.SetBool(winTriggerHash, true);                
                }
                if (teamRight) { // {0,5]
                    mAnimator.SetBool(looseTriggerHash, true);   
                }
            }
            else if (sliderValue < 3){
                if (teamLeft) {
                    mAnimator.SetBool(looseTriggerHash, true);                
                }
                if (teamRight) {
                    mAnimator.SetBool(winTriggerHash, true);   
                }   
            }
            else{
                mAnimator.SetBool(selectRandomAnimation(), true);
            }    
        } 


    }

    int selectRandomAnimation(){
        // Επιστρέφει τυχαία ένα απο τα id που υπάρχουν στον πίνακα
        int rIndex = Random.Range(0, totalRandomAnimations);
        int randomHash = hashAvailableAnims[rIndex];
        return randomHash;
    }
}
