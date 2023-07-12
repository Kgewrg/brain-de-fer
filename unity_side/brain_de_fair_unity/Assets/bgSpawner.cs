using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bgSpawner : MonoBehaviour
{

    public GameObject[] charPrefab_array;
    public GameObject centerPoint; 
    public int frontBackVariance; 
    public int leftRightVariance;



    // Define general spawn position (line behind main characters)
    private float spawnZ_line;   // Πόσο πίσω να είναι η πιο κοντινή γραμμή
    private float spawnLeftOffset; // ποσο αριστερά να ξεκινήσεις να spawnarei
    private float spawnY;   // Σε τι ύψος
    private float charSpace = 10;    // Space between characters
    

    public int n_chars = 12;
    private float tmp_frontBackOffset; 
    private float tmp_leftRightOffset;
 
 
    // Start is called before the first frame update
    void Start() {
        spawnZ_line = centerPoint.transform.position.z + 30;
        spawnLeftOffset = centerPoint.transform.position.x - 60;
        spawnY = centerPoint.transform.position.y - 13;

                
        spawnLine(0);
        spawnLine(10);
        spawnLine(20);
        spawnLine(30);

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
                    clone.GetComponent<bgChar_script>().teamA = true;
                }else{
                    clone.GetComponent<bgChar_script>().teamB = false;
                }
            }
        }
    }
}
