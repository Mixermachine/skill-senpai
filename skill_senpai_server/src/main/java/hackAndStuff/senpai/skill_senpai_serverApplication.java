package hackAndStuff.senpai;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

public class skill_senpai_serverApplication extends Application<skill_senpai_serverConfiguration> {

    public static void main(final String[] args) throws Exception {
        new skill_senpai_serverApplication().run(args);
    }

    @Override
    public String getName() {
        return "skill_senpai_server";
    }

    @Override
    public void initialize(final Bootstrap<skill_senpai_serverConfiguration> bootstrap) {
        // TODO: application initialization
    }

    @Override
    public void run(final skill_senpai_serverConfiguration configuration,
                    final Environment environment) {
        // TODO: implement application
    }

}
