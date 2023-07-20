using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgSpawner : MonoBehaviour
{

    public GameObject[] charPrefab_array;
    public GameObject centerPoint; 
    public float frontBackVariance; 
    public float leftRightVariance;



    // Define general spawn position (line behind main characters)
    private float spawnZ_line;   
    private float spawnLeftOffset;
    private float spawnY;   
    private float charSpace = 0.55f;    // Space between characters
    

    public int n_chars = 20;
    private float tmp_frontBackOffset; 
    private float tmp_leftRightOffset;
 
 
    // Start is called before the first frame update
    void Start() {
        spawnZ_line = centerPoint.transform.position.z + 2.5f;      // Πόσο πίσω να είναι η πιο κοντινή γραμμή
        spawnLeftOffset = centerPoint.transform.position.x - 3.5f;  // Ποσο αριστερα να ξεκινάνε οι χαρακτήρες
        spawnY = centerPoint.transform.position.y - 1.1f;           // Σε τι ύψος

                
        spawnLine(0);
        spawnLine(2);
        // spawnLine(4);
        // spawnLine(6);

    }

    // Update is called once per frame
    void Update() {
        
    }

    void spawnLine(int lineOffset){
        for (int i = 0; i < n_chars; i++) {

            // Get the randoms
            tmp_frontBackOffset = Random.Range(-frontBackVariance, frontBackVariance);
            tmp_leftRightOffset = Random.Range(-leftRightVariance, leftRightVariance);

            // Figure out spawn positions
            float spawnX = (float)(spawnLeftOffset + (i*charSpace));
            float spawnZ = (float)(spawnZ_line + tmp_frontBackOffset + lineOffset); 
            Vector3 spawnPos = new Vector3(spawnX, spawnY, spawnZ);

            // Select random model to spawn
            int randomModel =  Random.Range(0, charPrefab_array.Length);

            // Spawn the character
            GameObject clone = Instantiate(charPrefab_array[randomModel], spawnPos, Quaternion.identity, centerPoint.transform);

            // Get the angle between current character and center point
            var rot = Mathf.Atan2(spawnX - centerPoint.transform.position.x, spawnZ-centerPoint.transform.position.z) * Mathf.Rad2Deg;

            // Rotate the character
            clone.transform.Rotate(0f, rot+180, 0f);

            // Decide if the character will be animated or not
            int t = Random.Range(0,2);
            if (t == 1){
                clone.GetComponent<bgChar_script>().activeAnim = 1;

                int team = Random.Range(0,2);
                if (team == 1){
                    clone.GetComponent<bgChar_script>().teamLeft = true;
                }else{
                    clone.GetComponent<bgChar_script>().teamRight = true;
                }
            }
        }
    }
}
