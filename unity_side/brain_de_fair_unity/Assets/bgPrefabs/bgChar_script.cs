using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class bgChar_script : MonoBehaviour
{
    public int totalRandomAnimations = 3;
    public int activeAnim = 0; // Καθορίζει αν θα κάνει κάποιο animation
    public bool teamA;  // Καθορίζει σε ποια ομάδα θα είναι
    public bool teamB;
    public float minInterval = 5;
    public float maxInterval = 10;   
    private Animator mAnimator;


    // Πίνακας που περιέχει τα triggers των animations
    private List<int> hashAvailableAnims = new List<int>(); 

    void Start() { 
        mAnimator = GetComponent<Animator>();

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

        // Κάνει false όλα τα triggers ωστε να μην παίζουν επαναληπτικά
        foreach (int triggerHash in hashAvailableAnims) {
           mAnimator.SetBool(triggerHash, false);
        }
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
        if ((activeAnim == 1)){
            // Debug.Log("playing Anim");
            mAnimator.SetBool(selectRandomAnimation(), true);
        } 


    }

    int selectRandomAnimation(){
        // Επιστρέφει τυχαία ένα απο τα id που υπάρχουν στον πίνακα
        int rIndex = Random.Range(0, totalRandomAnimations);
        int randomHash = hashAvailableAnims[rIndex];
        return randomHash;
    }
}
