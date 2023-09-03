
using System.Diagnostics;
using UnityEngine;


public class eggConnectionScript : MonoBehaviour
{

    // TODO: Να μπορείς να διαλέξεις recoderd (μέσο player prefs)
    // 
    private string interpeterPath = "C:\\Users\\tsarosDesktop\\AppData\\Local\\Microsoft\\WindowsApps\\python3.10.exe";
    
    public static int classifierSelector = 0; // 0: device classifier, 1: ML classifier
    private string deviceClassifier = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\python_side\\recorderOriginal.py";
    private string ML_classifier = "C:\\Users\\tsarosDesktop\\Documents\\repositories\\brain-de-fair\\python_side\\recorderML.py";

    private string scriptPath;
    Process pyProcess = new Process();

    static eggConnectionScript instance;    

    void Awake() {
        
        // Για να μην διαγράφεται στο reload
        if (instance != null){
            Destroy(gameObject);
        }
        else{
            instance = this;
            DontDestroyOnLoad(gameObject);
        }

        if (PlayerPrefs.GetInt("classifier", -1) == 0){
            scriptPath = deviceClassifier;
        }
        else if (PlayerPrefs.GetInt("classifier", -1) == 1){
            scriptPath = ML_classifier;
        }
        else {
            UnityEngine.Debug.LogError("Error selecting classifier");
        }
        

        ProcessStartInfo startInfo = new ProcessStartInfo();
        startInfo.FileName = interpeterPath;
        startInfo.Arguments = scriptPath;
        startInfo.UseShellExecute = false;
        startInfo.RedirectStandardOutput = true;
        startInfo.CreateNoWindow = true;

        pyProcess.StartInfo = startInfo;
        pyProcess.Start();
    }



    void OnDestroy(){
        // Κλείνει το python όταν σταματάει το παιχνίδι 
        if (pyProcess != null && !pyProcess.HasExited) {
            pyProcess.Kill();
            pyProcess.Close();
            pyProcess.Dispose();
        }
    }
}
