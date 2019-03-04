import java.io.*;
import javax.swing.*;
import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;

class Window
{
    JFrame f;
    JLabel[] cli;
    JLabel face;
    JLabel chat;
    String cliText;
    String cliBuff;

    KeyListener k;

    Window()
    {
        f = new JFrame("Theara");
        f.setSize(1300,730);
        f.setLayout(null);
        f.setResizable(false);
        createChat();
        createFace();
        createCli();
        addKeyListener();
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    void createCli()
    {
        cli = new JLabel[8];
        for (int i=0; i<8; i++)
        {
            cli[i] = new JLabel("");
            cli[i].setBounds(337,530+(20*i),953,20);
            cli[i].setFont(new Font(Font.MONOSPACED, cli[i].getFont().getStyle(), 17));
            cli[i].setOpaque(true);
            cli[i].setBackground(new Color(0,0,0));
            cli[i].setForeground(new Color(0,200,0));
        }
        cliText = "";
        cliBuff = ">>> ";
        for (int i=0; i<8; i++)
            f.add(cli[i]);
        cli[7].setText(">>> ");
    }

    void addKeyListener()
    {
        k = new KeyListener()
        {
            @Override
            public void keyTyped(KeyEvent key)
            {
                //System.out.println("Key typed code=" + key.getKeyCode() + ", char=" + key.getKeyChar());
                char temp = key.getKeyChar();
                editCli(temp);
            }

            @Override
            public void keyPressed(KeyEvent key)
            {
                //System.out.println("Key pressed code=" + key.getKeyCode() + ", char=" + key.getKeyChar());
            }

            @Override
            public void keyReleased(KeyEvent key)
            {
                //System.out.println("Key released code=" + key.getKeyCode() + ", char=" + key.getKeyChar());
            }
        };

        f.addKeyListener(k);
    }

    void editCli(char temp)
    {
        if((temp>=(char)32&&temp<=(char)126))
            cliBuff += temp;
        else if(temp==8)
        {    
            try
            {
                cliBuff = cliBuff.substring(0, cliBuff.length()-1);
            }
            catch (java.lang.StringIndexOutOfBoundsException ex){}
        }
        else if (temp == '\n') 
        {
            if(cliBuff.length()<85)
                cliText += (cliBuff + '\n');
            else
            {
                cliText += (cliBuff.substring(0,85) + "\n");
                cliText += (cliBuff.substring(85, cliBuff.length()) + "\n");
            }
            callBash();
            cliBuff = ">>> ";
        }
        setCliText();
    }

    void setCliText()
    {
        int m=0,n=0;
        String[] cliLines = cliText.split("\n", 0);
        m = cliLines.length;
        String cli2ndLastLine;
        String cliLastLine;
        if (cliBuff.length()>85)
        {
            cliLastLine    = cliBuff.substring(85, cliBuff.length());
            cli2ndLastLine = cliBuff.substring(0,85);
            n=2;
        }
        else
        {
            cliLastLine    = cliBuff;
            cli2ndLastLine = "";
            n=1;
        }
        if (m+n>8)
        {
            if (n==1)
            {
                cli[7].setText(cliBuff);
                for(int i=0;i<7;i++)
                {
                    cli[i].setText(cliLines[m-7+i]);
                }
            }
            else if(n==2)
            {
                cli[7].setText(cliLastLine);
                cli[6].setText(cli2ndLastLine);
                for(int i=0;i<6;i++)
                {
                    cli[i].setText(cliLines[m-6+i]);
                }
            }
        }
        else
        {
            if (n==1)
            {
                cli[7].setText(cliBuff);
                for(int i=0;i<m;i++)
                {
                    cli[7-m+i].setText(cliLines[i]);
                }
            }
            else if(n==2)
            {
                cli[7].setText(cliLastLine);
                cli[6].setText(cli2ndLastLine);
                for(int i=0;i<m;i++)
                {
                    cli[6-m+i].setText(cliLines[i]);
                }
            }

        }
            
    }

    void callBash()
    {
        System.out.println(cliBuff + " executed");
    }

    void createChat()
    {
        chat = new JLabel("jlvkhrkl");
        chat.setBounds(10,10,317,680);
        Font f1 = chat.getFont();
        Font f2 = new Font(f1.getFontName(), f1.getStyle(), f1.getSize()+5);
        chat.setFont(f2);
        chat.setOpaque(true);
        chat.setBackground(new Color(0,0,0));
        chat.setForeground(new Color(0,0,255));
        f.add(chat);
    }

    void createFace()
    {
        BufferedImage myPicture;
        try
        {
            myPicture = ImageIO.read(new File("/home/akarsh/Ashu backup 2/Desktop/safe_image_thumb.gif"));
            face = new JLabel(new ImageIcon(myPicture));
        }
        catch(IOException e)
        {
            face = new JLabel();
        }
        face.setBounds(337,10,953,510);
        face.setOpaque(true);
        face.setBackground(new Color(0,0,0));

        f.add(face);
    }
}


class Main
{
    public static void main(String[] args)
    {
        new Window();
    }
}