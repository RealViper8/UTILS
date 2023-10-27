import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.event.ActionListener;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.io.File;
import javax.swing.UIManager;


public class menu {
    private static JLabel statusLabel;

    public static void main(String[] args) {
        try { 
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            e.printStackTrace();
        }
        JPanel panel = new JPanel();
        JFrame frame = new JFrame();
        frame.setSize(100,100);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Menu");
        frame.add(panel);
        
        panel.setLayout(null);

        JButton launch = new JButton("Launch UTILS");
        launch.setForeground(Color.GRAY);
        launch.setBounds(20, 20, 170, 25);
        panel.add(launch);

        JButton pip = new JButton("Update pip");
        pip.setForeground(Color.BLUE);
        pip.setBounds(20, 50, 170, 25);
        panel.add(pip);

        JButton install = new JButton("Install requirements");
        install.setForeground(Color.GRAY);
        install.setBounds(20, 80, 170, 25);
        panel.add(install);

        JButton exit = new JButton("Exit");
        exit.setForeground(Color.RED);
        exit.setBounds(20, 110, 170, 25);
        panel.add(exit);

        statusLabel = new JLabel("--------");
        statusLabel.setBounds(85, 140, 100, 25);
        statusLabel.setForeground(Color.black);
        panel.add(statusLabel);

        frame.setSize(230, 200);
        //panel.setBackground(Color.DARK_GRAY);
        frame.setMinimumSize(new Dimension(230,200));
        frame.setMaximumSize(new Dimension(240,250));
        frame.setResizable(true);
        //frame.requestFocus();
        frame.setResizable(false);
        frame.setAlwaysOnTop(true);

        frame.setVisible(true);

        exit.addActionListener(new ActionListener () {
            public void actionPerformed(ActionEvent e) {
                System.out.println("\n[-] Exiting\n     Code 0");
                System.exit(0);
            }
        });

        launch.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                statusLabel.setText("Launched UTILS");
                statusLabel.setBounds(65, 140, 100, 25);
                try
                { 
                    File f = new File("utils.exe");

                    if(f.isFile() && !f.isDirectory()) { 
                        System.out.println("\n[*] Found utils.exe\n[*] Trying to Launch");
                        Runtime.getRuntime().exec(new String[] {"cmd", "/k", "start", "utils.exe"}); 
                    } else {
                        System.out.println("\n[*] Found main.py\n[*] Trying to Launch");
                        Runtime.getRuntime().exec(new String[] {"cmd", "/k", "start", "python", "main.py"});
                    }
                } 
                catch (Exception er) 
                { 
                    System.out.println("Something Wrong Happend"); 
                    er.printStackTrace(); 
                } 
            }
        });

        pip.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                statusLabel.setText("Upgraded PIP");
                statusLabel.setBounds(70, 140, 100, 25);
                try
                { 
                    Runtime.getRuntime().exec(new String[] {"cmd", "/k", "start", "python", "-m", "pip", "install", "--upgrade", "pip"}); 
                } 
                catch (Exception er)
                { 
                    System.out.println("Something Wrong Happend"); 
                    er.printStackTrace(); 
                }
            }
        });

        install.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) { 
                try
                { 
                    statusLabel.setText("Installed Requirements");
                    statusLabel.setBounds(45, 140, 150, 25);
                    Runtime.getRuntime().exec(new String[] {"cmd", "/k", "start", "python", "-m", "pip", "install", "-r", "requirements.txt"});
                    //statusLabel.setText("--------");
                } 
                catch (Exception er)
                { 
                    statusLabel.setText("--------");
                    System.out.println("Something Wrong Happend"); 
                    er.printStackTrace(); 
                }
            }
        });
    }
}